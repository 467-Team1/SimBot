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
include src/CMakeFiles/lm_test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/lm_test.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/lm_test.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/lm_test.dir/flags.make

src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o: src/CMakeFiles/lm_test.dir/flags.make
src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o: /Users/laasyachukka/Documents/W_24/EECS\ 467/streaming/AprilTag/src/contrib/lm_test.cpp
src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o: src/CMakeFiles/lm_test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir="/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o -MF CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.d -o CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o -c "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src/contrib/lm_test.cpp"

src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/lm_test.dir/contrib/lm_test.cpp.i"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src/contrib/lm_test.cpp" > CMakeFiles/lm_test.dir/contrib/lm_test.cpp.i

src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/lm_test.dir/contrib/lm_test.cpp.s"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src/contrib/lm_test.cpp" -o CMakeFiles/lm_test.dir/contrib/lm_test.cpp.s

# Object files for target lm_test
lm_test_OBJECTS = \
"CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o"

# External object files for target lm_test
lm_test_EXTERNAL_OBJECTS =

bin/lm_test: src/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o
bin/lm_test: src/CMakeFiles/lm_test.dir/build.make
bin/lm_test: lib/libapriltag.dylib
bin/lm_test: src/CMakeFiles/lm_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir="/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../bin/lm_test"
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lm_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/lm_test.dir/build: bin/lm_test
.PHONY : src/CMakeFiles/lm_test.dir/build

src/CMakeFiles/lm_test.dir/clean:
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" && $(CMAKE_COMMAND) -P CMakeFiles/lm_test.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/lm_test.dir/clean

src/CMakeFiles/lm_test.dir/depend:
	cd "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/src" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src" "/Users/laasyachukka/Documents/W_24/EECS 467/streaming/AprilTag/build/src/CMakeFiles/lm_test.dir/DependInfo.cmake" "--color=$(COLOR)"
.PHONY : src/CMakeFiles/lm_test.dir/depend

