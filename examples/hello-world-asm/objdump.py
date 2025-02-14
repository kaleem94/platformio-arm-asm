import os
Import("env","projenv")

def make_something(source, target, env):
#    print(projenv.Dump())
    builddir = env['PROJECT_BUILD_DIR']+"/"+env['PIOPLATFORM']
    srcdir = env['PROJECT_SRC_DIR']+"/"
    for x in source:
        name, ext = os.path.splitext(x.name)
        objfile = builddir+"/src/"+x.name
        lssfile = srcdir+name+".lss"
        env.Execute("arm-none-eabi-objdump -d /"+objfile+" -l > "+lssfile)

env.AddPostAction("$BUILD_DIR/${PROGNAME}.elf", make_something)

env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction("arm-none-eabi-objdump -h -S $BUILD_DIR/${PROGNAME}.elf > $BUILD_DIR/${PROGNAME}.lss",
    # env.VerboseAction("arm-none-eabi-objdump -Mno-aliases,numeric -h -S $BUILD_DIR/${PROGNAME}.elf > $BUILD_DIR/${PROGNAME}.lss",
    "Creating $BUILD_DIR/${PROGNAME}.lss")
)
