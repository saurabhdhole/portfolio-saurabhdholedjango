from django.shortcuts import render

# Create your views here.
from portfolio.models import Project
from django.http import HttpResponse
from django.template import loader

def indexPage(request):
    return render(request,"index.html")

def projects(request, project_name):
    projectList = [ Project("2dDrafting", "2D Drafting application", "Developer", "Vb.Net, Eyeshot", "The lightweight library which provides AutoCAD OEM module with Eyeshot. Features like command line utility, drawing, Layer and editing features."),
                    Project("3dDrafting", "3D Graphical User Interface", "Developer", "C#.Net, Eyeshot", "Provided WinForm based thread safe solution which provides better 3D view with more features like WinForm controller, custom entity, selection filter, etc."),
                    Project("vanity", "Vanity", "Research And Developer", "C#.Net, ASP.NET", "Provided webform based solution that scan QR code and super imposed model infront of QR."),
                    Project("custom_insole_designer", "Custom Insole Designer", "Developer", "C#.Net, Eyeshot", "Provided WinForm based solution to generate the insole for scanned human foot. Also provided trimming, solidify, alignment and Mesh deformation (mapped 2D curvature to 3D surface). Generated machine code of insole for CNC machine."),
                    Project("body_measuring", "Body Measuring Application", "Research And Developer", "C#.Net, Eyeshot", "Provided Eyeshot based solution to automate alignment of human leg in Z+ direction and Patella in X+ direction. Also, automatic determination of patella point, knee point and ankle point."),
                    Project("cad_generate_and_view", "CAD Generate and View", "Research And Developer", "Eyeshot, Hoops, ACIS, Teigha, C#, C++, JavaScript, HTML, ASP.NET", "Research based project to figure out 10 years ahead product and technology. Investigated Eyeshot, Hoops Communicator, ACIS and Teigha technologies. Generated 3D model and annotations and stored all available formats. From 3D drawing created 2D drawing of model (Top, Front and ISO views). Generated hoops xml from BXF file to views and configure models."),
                    Project("fbx_exporter", "FBX Exporter ", "Developer", "C#.Net, C++, Autodesk FBX SDK", "Plugin to export the Fusion360 models into FBX file format."),
                    Project("json_library", "JSON Library", "Developer", "C#.Net, THREE.JS", "Developed JSON library to export JSON format 4.5 on the top of PTS library. JSON library supports to visibility of nodes, face level color support, cumulative transformation and face level transparency."),
                    Project("voice_360", "VOICE 360 (2 Month)", "Developer & Mentor", "HTML, CSS, JavaScript, Forge, BIM 360, PHP, ASP.NET", "Voice 360 is an application which allows you to interact with Forge Viewer and BIM 360 model using voice. It provides voice recognition feature to execute Forge Viewer commands. With the help of microphone on your system, you can give commands instead of taking inputs from mouse and keyboard. This application seamlessly integrates with an existing system and can be extended with more commands as needed. Successfully submitted the application to BIM360 Autodesk Hackathon.(http://dev.prototechsolutions.com:83/ps/voice360/index.html)"),
                    Project("autodesk_platform_plugins", "Autodesk Platform Plugins", "Developer", "C#.NET, C++", "Project consists of 3DPDF, OBJ and WebGL exporter’s plugins for major Autodesk Platforms like Inventor, AutoCAD, Revit.")
                ]
    for proj in projectList:
        if proj.id == project_name:
            output = proj
            break

    #output = projectList[0]

    context = {'output': output}

    return render(request, 'project_t.html', context)

    #return HttpResponse(template.render(context, request))

