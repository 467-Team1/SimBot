# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.28.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.28.1/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build"

# Include any dependencies generated for this target.
include src/CMakeFiles/apriltag_demo.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/apriltag_demo.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/apriltag_demo.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/apriltag_demo.dir/flags.make

src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o: src/CMakeFiles/apriltag_demo.dir/flags.make
src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o: /Users/laasyachukka/Documents/W_24/EECS\ 467/streaming/AprilTag/src/apriltag_demo.c
src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o: src/CMakeFiles/apriltag_demo.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir="/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o -MF CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o.d -o CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o -c "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src/apriltag_demo.c"

src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/apriltag_demo.dir/apriltag_demo.c.i"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src/apriltag_demo.c" > CMakeFiles/apriltag_demo.dir/apriltag_demo.c.i

src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/apriltag_demo.dir/apriltag_demo.c.s"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src/apriltag_demo.c" -o CMakeFiles/apriltag_demo.dir/apriltag_demo.c.s

# Object files for target apriltag_demo
apriltag_demo_OBJECTS = \
"CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o"

# External object files for target apriltag_demo
apriltag_demo_EXTERNAL_OBJECTS =

bin/apriltag_demo: src/CMakeFiles/apriltag_demo.dir/apriltag_demo.c.o
bin/apriltag_demo: src/CMakeFiles/apriltag_demo.dir/build.make
bin/apriltag_demo: lib/libapriltag.dylib
bin/apriltag_demo: src/CMakeFiles/apriltag_demo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir="/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../bin/apriltag_demo"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/apriltag_demo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/apriltag_demo.dir/build: bin/apriltag_demo
.PHONY : src/CMakeFiles/apriltag_demo.dir/build

src/CMakeFiles/apriltag_demo.dir/clean:
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && $(CMAKE_COMMAND) -P CMakeFiles/apriltag_demo.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/apriltag_demo.dir/clean

src/CMakeFiles/apriltag_demo.dir/depend:
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src/CMakeFiles/apriltag_demo.dir/DependInfo.cmake" "--color=$(COLOR)"
.PHONY : src/CMakeFiles/apriltag_demo.dir/depend

