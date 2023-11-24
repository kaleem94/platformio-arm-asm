# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import join
from SCons.Script import (ARGUMENTS, COMMAND_LINE_TARGETS, AlwaysBuild,
                          Builder, Default, DefaultEnvironment)

env = DefaultEnvironment()

env.Replace(
    _BINPREFIX="",
    AR="${_BINPREFIX}ar",
    AS="${_BINPREFIX}as",
    CC="${_BINPREFIX}gcc",
    GDB="gdb-multiarch",
    CXX="${_BINPREFIX}g++",
    OBJCOPY="${_BINPREFIX}objcopy",
    RANLIB="${_BINPREFIX}ranlib",
    SIZETOOL="${_BINPREFIX}size",
    OBJDUMP="${_BINPREFIX}objdump",


    ARFLAGS=["rc"],

    SIZEPRINTCMD='$SIZETOOL -d $SOURCES',

    PROGSUFFIX=".elf",
    PROGNAME="firmware"
)

pioframework = env.get("PIOFRAMEWORK", [])
if "glibc" in pioframework:
    env.Replace(_BINPREFIX="arm-linux-gnueabihf-")
else: 
    env.Replace(_BINPREFIX="arm-none-eabi-")

#
# Target: Build elf only
#
target_elf = env.BuildProgram()

#
# Target: Print binary size
#
target_size = env.Alias(
    "size", target_elf,
    env.VerboseAction("$SIZEPRINTCMD", "Calculating size $SOURCE"))
AlwaysBuild(target_size)

#
# Setup default targets
#

Default([target_elf, target_size])
