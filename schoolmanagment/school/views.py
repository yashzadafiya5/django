from django.http import HttpResponse
from django.shortcuts import render
import h11

# Create your views here.


def home(request):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

</head>
<body>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">home page</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="home">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="aboutus">aboutus</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="gallery">gallery</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="vidos">vidos</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="contactus">contactus</a>
              </li>
             
            </ul>
            <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>
        <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>

</body>
</html>''')
def aboutus(request):
    return HttpResponse('''<h1>about us</h1><br><hr> <a href='home'>home</a>&nbsp;&nbsp; <a href='aboutus'>aboutus</a> &nbsp;&nbsp; <a href='gallery'>gallery</a> &nbsp;&nbsp;<a href='vidos'>vidos</a>&nbsp;&nbsp; <a href='contactus'>contactus</a>''')
def gallery(request):
    return HttpResponse('''<h1>gallery</h1><br><hr><a href='home'>home</a>&nbsp;&nbsp; <a href='aboutus'>aboutus</a> &nbsp;&nbsp; <a href='gallery'>gallery</a> &nbsp;&nbsp;<a href='vidos'>vidos</a>&nbsp;&nbsp; <a href='contactus'>contactus</a>''')
def vidos(request):
    return HttpResponse('''<h1>vidos page</h1><br><hr> <a href='home'>home</a>&nbsp;&nbsp; <a href='aboutus'>aboutus</a> &nbsp;&nbsp; <a href='gallery'>gallery</a> &nbsp;&nbsp; <a href='vidos'>vidos</a>&nbsp;&nbsp; <a href='contactus'>contactus</a>''')
def contactus(request):
    return HttpResponse('''<h1>contact us</h1><br><hr><a href='home'>home</a>&nbsp;&nbsp; <a href='aboutus'>aboutus</a> &nbsp;&nbsp; <a href='gallery'>gallery</a> &nbsp;&nbsp;<a href='vidos'>vidos</a>&nbsp;&nbsp; <a href='contactus'>contactus</a>''')

