Import("env")

env.Append(
    LINKFLAGS=[
        "-nostdlib",
        "-static"
        ]
)
