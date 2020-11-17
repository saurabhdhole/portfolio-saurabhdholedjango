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
                    Project("cad_generate_and_view", "", "Developer", "", ""),
                    Project("fbx_exporter", "", "Developer", "", ""),
                    Project("json_library", "", "Developer", "", ""),
                    Project("voice_360", "", "Developer", "", ""),
                    Project("autodesk_platform_plugins", "", "Developer", "", "")
                ]
    for proj in projectList:
        if proj.id == project_name:
            output = proj
            break

    #output = projectList[0]

    context = {'output': output}

    return render(request, 'project_t.html', context)

    #return HttpResponse(template.render(context, request))

