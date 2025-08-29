
# Hello C#

- [Hello C#](#hello-c)
  - [Understanding top-level programs](#understanding-top-level-programs)
  - [Implicitly imported namespaces](#implicitly-imported-namespaces)
  - [Project template names](#project-template-names)

## Understanding top-level programs

- `dotnet new console --use-program-main`

```csharp
using System;
namespace HelloCS
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine('Hello, World!');
    }
  }
}
```
- Key points to remember about top-level programs include the following:
  -   There can be only one file like this in a project.
  -   Any `using` statements must be at the top of the file.
  -   If you declare any classes or other types, they must be at the bottom of the file.
  -   Although you should name the method `Main` if you explicitly define it, the method is named `<Main>$` when created by the compiler.

## Implicitly imported namespaces


## Project template names

| **Visual Studio 2022** | **dotnet new** | **JetBrains Rider - Type** |
| --- |  --- |  --- |
| Console App | `console` | Console Application |
| Class Library | `classlib` | Class Library |
| xUnit Test Project | `xunit` | Unit Test Project - xUnit |
| ASP.NET Core Empty | `web` | ASP.NET Core Web Application - Empty |
| Razor Class Library | `razorclasslib` | ASP.NET Core Web Application - Razor Class Library |
| ASP.NET Core Web App (Model-View-Controller) | `mvc` | ASP.NET Core Web Application - Web App (Model-View-Controller) |
| ASP.NET Core Web API | `webapi` | ASP.NET Core Web Application - Web API |
| ASP.NET Core Web API (native AOT) | `webapiaot` | ASP.NET Core Web Application - Web API (native AOT) |
| Blazor Web App | `blazor` | ASP.NET Core Web Application - Blazor Web App |