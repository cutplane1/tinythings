static import core.exception;
import std.stdio;
import std.file;

void main(string[] args)
{
    try
    {
    writeln(cast(string)read(args[1]));
    }
    catch (FileException e)
    {
        writeln("err: no such file exists");
    }
    catch (core.exception.ArrayIndexError e)
    {
        writeln("err: no file provided. usage: cat <filename>");
    }
}