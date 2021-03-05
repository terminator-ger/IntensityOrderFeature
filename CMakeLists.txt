cmake_minimum_required(VERSION 2.8)
project(XIOP)

find_package(OpenCV 4.0 REQUIRED COMPONENTS core highgui)
inlcude_directories(${OpenCV_INCLUDE_DIRS})

set(SOURCE src/*.cpp)
set(HEADERS inlcude/*.h
            ${OpenCV_INCLUDE_DIRS})

set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_LIST_DIR}/pyXIOP/lib/linux)
ADD_LIBRARY(${PROEJCT_NAME} SHARED ${SOURCE})
target_link_libraries(${PROEJCT_NAME} ${OpenCV_LIBS})