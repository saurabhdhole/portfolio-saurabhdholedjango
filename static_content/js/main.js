
$(document).ready(function () {
    // Initialize Tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // Add smooth scrolling to all links in navbar + footer link
    $(".navbar a, footer a[href='#myPage']").on('click', function (event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {

            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 900, function () {

                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
            });
        } // End if
    });

   // main();
})
function openModalPop(projectPage) {

    document.getElementById("myframe").src = "projects/"+ projectPage;
//    if (projectPage == "2dDrafting") {
//        document.getElementById("myframe").src = "projects/2dDrafting";
//    }
//    else if (projectPage == "3dDrafting") {
//        document.getElementById("myframe").src = "projects/3dDrafting";
//    }
//    else if (projectPage == "vanity") {
//        document.getElementById("myframe").src = "projects/vanity";
//    }
//    else if (projectPage == "custom_insole_designer") {
//        document.getElementById("myframe").src = "projects/custom_insole_designer";
//    }
//    else if (projectPage == "body_measuring") {
//        document.getElementById("myframe").src = "projects/body_measuring";
//    }
//    else if (projectPage == "cad_generate_and_view") {
//        document.getElementById("myframe").src = "projects/cad_generate_and_view";
//    }
//    else if (projectPage == "fbx_exporter") {
//        document.getElementById("myframe").src = "projects/fbx_exporter";
//    }
//    else if (projectPage == "json_library") {
//        document.getElementById("myframe").src = "projects/json_library";
//    }
//    else if (projectPage == "voice_360") {
//        document.getElementById("myframe").src = "projects/voice_360";
//    }
//    else if (projectPage == "autodesk_platform_plugins") {
//        document.getElementById("myframe").src = "projects/autodesk_platform_plugins";
//    }

    $('#myModal').modal('show');
}

function sendMailToSaurabhDhole() {
    var service_id = 'gmail';
    var template_id = 'template_apHJWTEf';
    var template_params = {
        "reply_to": document.getElementById('email').value,
        "from_name": document.getElementById('name').value,
        "to_name": "Saurabh Dhole",
        "message_html": document.getElementById('comments').value
    };
    emailjs.send(service_id, template_id, template_params);

    document.getElementById('email').value = '';
    document.getElementById('name').value = '';
    document.getElementById('comments').value = '';
}

function main() {
    const canvas = document.querySelector('#c');
    const renderer = new THREE.WebGLRenderer({
        canvas,
        alpha: true,
    });

    const fov = 75;
    const aspect = 2;  // the canvas default
    const near = 0.1;
    const far = 5;
    const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
    camera.position.z = 2;

    const scene = new THREE.Scene();

    {
        const color = 0xFFFFFF;
        const intensity = 1;
        const light = new THREE.DirectionalLight(color, intensity);
        light.position.set(-1, 2, 4);
        scene.add(light);
    }

    const boxWidth = 1;
    const boxHeight = 1;
    const boxDepth = 1;
    const geometry = new THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);

    var loader = new THREE.FontLoader();

    loader.load('fonts/helvetiker_regular.typeface.json', function (font) {

        var saurabhdholetext = new THREE.TextGeometry('Hello three.js!', {
            font: font,
            size: 80,
            height: 5,
            curveSegments: 12,
            bevelEnabled: true,
            bevelThickness: 10,
            bevelSize: 8,
            bevelOffset: 0,
            bevelSegments: 5
        });

        scene.add(saurabhdholetext);

    });

    const textmaterial = new THREE.MeshPhongMaterial({ color:0xffffff });
    


    function makeInstance(geometry, color, x) {
        const material = new THREE.MeshPhongMaterial({ color });

        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        cube.position.x = x;

        return cube;
    }

    const cubes = [
        //makeInstance(geometry, 0x44aa88, 0),
        //makeInstance(geometry, 0x8844aa, -2),
        //makeInstance(geometry, 0xaa8844, 2),
    ];

    function resizeRendererToDisplaySize(renderer) {
        const canvas = renderer.domElement;
        const width = canvas.clientWidth;
        const height = canvas.clientHeight;
        const needResize = canvas.width !== width || canvas.height !== height;
        if (needResize) {
            renderer.setSize(width, height, false);
        }
        return needResize;
    }

    function render(time) {
        time *= 0.001;

        if (resizeRendererToDisplaySize(renderer)) {
            const canvas = renderer.domElement;
            camera.aspect = canvas.clientWidth / canvas.clientHeight;
            camera.updateProjectionMatrix();
        }

        //cubes.forEach((cube, ndx) => {
        //    const speed = 1 + ndx * .1;
        //    const rot = time * speed;
        //    cube.rotation.x = rot;
        //    cube.rotation.y = rot;
        //});

        renderer.render(scene, camera);

        //requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
}


