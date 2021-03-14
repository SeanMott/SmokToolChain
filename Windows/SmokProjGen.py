#genarates a smok project premake file

import sys
import os

#args formate || progName progDefineName
#example || python SmokProjGen.py Pong PONG
#example || python SmokProjGen.py Invaders INV
#example || python SmokProjGen.py Snake SNAKE
#example || python SmokProjGen.py Tetris TETRIS

progName = sys.argv[1]
progDefine = sys.argv[2]

#makes the project directory and it's base files
os.makedirs(progName + "/src", exist_ok= True)
os.makedirs(progName + "/src/Widgets", exist_ok= True)
os.makedirs(progName + "/src/Systems", exist_ok= True)
os.makedirs(progName + "/src/Components", exist_ok= True)
os.makedirs(progName + "/src/Scripts", exist_ok= True)
os.makedirs(progName + "/res", exist_ok= True)
os.makedirs(progName + "/res/Shaders", exist_ok= True)
os.makedirs(progName + "/res/Textures", exist_ok= True)
os.makedirs(progName + "/res/Models", exist_ok= True)
os.makedirs(progName + "/res/Scenes", exist_ok= True)
os.makedirs(progName + "/res/Prefabs", exist_ok= True)
os.makedirs(progName + "/res/Audio", exist_ok= True)

#writes main
file = open(progName + "/src/main.cpp", "w+")
file.write("//Engine\n#include <Smok/Core/Engine>\n\n//" + progName + """\n\n//Other\n\nint main(int args, char*argv[])
{
    Smok::Core::EngineCreateInfo engineInfo;
    Smok::Core::Application app;
    app.Init(info);
    app.Run();
    app.Destroy();
    return 0;
}""")
file.close()

#writes the project premake file
file = open(progName + "/premake5.lua", "w+")
file.write("""workspace \"""" + progName + """\"
    architecture "x86"

    configurations
    {
        "Debug",
        "Release",
        "Dist"
    }

project \"""" + progName + """\"
    kind "ConsoleApp"
    language "C++"

    targetdir ("bin/%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}/%{prj.name}")
    objdir ("bin-obj/%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}/%{prj.name}")


    files 
    {
        "src/**.h",
        "src/**.c",
        "src/**.hpp",
        "src/**.cpp",
    }
    
    includedirs
    {
        
        "Library/Smok/Library/glm/glm",
        "Library/Smok/Library/Glfix/Glfix/includes",
        "Library/Smok/Library/ImGUI",
        "Library/Smok/includes",
        "src",
        
    }
    
    links
    {
        "Smok"
    }

    defines
    {
        "GLFW_INCLUDE_NONE",
        "GLM_FORCE_RADIANS",
        "GLM_FORCE_DEPTH_ZERO_TO_ONE",
    }

    flags
    {
        "MultiProcessorCompile"
    }

    --stops C files from needing the PCH file
    filter "files:src/**.c"
    flags {"NoPCH"}

    filter "system:windows"
        cppdialect "C++17"
        staticruntime "On"
        systemversion "latest"
    
        defines
        {
            "Window_Build",
            "Desktop_Build"
        }
    
    filter "configurations:Debug"
        defines \"""" + progDefine + """_DEBUG"
        symbols "On"
    
    filter "configurations:Release"
        defines \"""" + progDefine + """_RELEASE"
        optimize "On"
    
    filter "configurations:Dist"
        defines \"""" + progDefine + """_DIST"
        optimize "On"

        --removes the widgets in Dist builds
        removefiles
        {
            "src/Widgets/**.h",
            "src/Widgets/**.c",
            "src/Widgets/**.hpp",
            "src/Widgets/**.cpp",
        }

        flags
        {
            "LinkTimeOptimization"
        }
""")