package test

import java.io.File
import java.nio.file.Path



//Verify folder
fun isFolder(path: String): Boolean {
    var file = File(path) //Create file object

    return file.isDirectory //Return true if is folder else false
}

fun hasFile(path: String): Boolean {
    var file = File(path)
    var files = file.list() //Get file names into array

    return files.isEmpty() //Return true folder contain any file else false
}

fun getName(path: String): Boolean {
    var file = File(path)
    var files = file.list()

    if(files.isNotEmpty()) //If true, proceed to print file names and directories
    {
        //For loop to print filename and directory name
        for (file in files) {
            println(files)
        }
    }
    else
    {
        return false //Folder does not contain any file
    }

    return true
}

fun createFile(name: String): Boolean {
    var file = File(name)

    return file.createNewFile() //Return true if file is created.
}

fun createFolder(name: String): Boolean {
    var file = File(name)

    return file.mkdir() //Return true if folder is created.
}

fun main(args: Array<String>) {
    //Display options
    println("Please select an option:")
    println("1. Folder verification")
    println("2. File verification")
    println("3. Get file name from path")
    println("4. Create file")
    println("5. Create folder")

    //Get option from user input
    val option = readLine()!!.trim().toInt()

    //Options with if else statement
    if(option == 1)
    {
        println("Please enter a path:")

        //Get path from user input
        val path = readLine()!!.trim()

        if(isFolder(path)) //True
        {
            println("$path is a folder.")
        }
        else //False
        {
            println("$path is not a folder.")
        }
    }
    else if(option == 2)
    {
        println("Please enter a path:")
        val path = readLine()!!.trim()

        if(hasFile(path)) //True
        {
            println("$path has files.")
        }
        else //False
        {
            println("$path has no file.")
        }
    }
    else if(option == 3)
    {
        println("Please enter a path:")
        val path = readLine()!!.trim()

        if(!getName(path)) //False
        {
            println("No file in $path.")
        }
    }
    else if(option == 4)
    {
        println("Please enter a file name:")
        val name = readLine()!!

        if(createFile(name)) //True
        {
            println("File created successfully.")
        }
        else //False
        {
            println("File already exists.")
        }
    }
    else if(option == 5)
    {
        println("Please enter a folder name:")
        val name = readLine()!!

        if(createFolder(name)) //True
        {
            println("Folder created successfully.")
        }
        else //False
        {
            println("Folder already exists.")
        }
    }
    //If user input is invalid.
    else
    {
        println("Invalid option.")
    }

    val scanner = readLine() //Hold system until user input something.
}
