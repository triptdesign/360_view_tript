function updateTitle(title){

    document
    .getElementById(
        'sceneTitle'
    )
    .innerText = title;

}

function createNavigation(){

    const bottomNav =
    document.getElementById(
        'bottomNav'
    );
    
    const navLeft =
    document.getElementById(
        'navLeft'
    );

    const navRight =
    document.getElementById(
    'navRight'
    );

    bottomNav.innerHTML = '';
    
    // =========================================
    // LEFT BUTTON
    // =========================================

    navLeft.onclick = ()=>{
    
        bottomNav.scrollBy({
        
            left:-250,
        
            behavior:'smooth'
        
        });
    
    };
    
    // =========================================
    // RIGHT BUTTON
    // =========================================
    
    navRight.onclick = ()=>{
    
        bottomNav.scrollBy({
        
            left:250,
        
            behavior:'smooth'
        
        });
    
    };
    
    // =========================================
    // MOUSE WHEEL SCROLL
    // =========================================
    
    bottomNav.addEventListener(
        'wheel',
        (event)=>{
        
            event.preventDefault();
        
            bottomNav.scrollLeft +=
            event.deltaY;
        
        }
    );
        

    window.PANORAMA_SCENES
    .forEach(
        (
            scene,
            index
        )=>{

        const button =
        document.createElement(
            'button'
        );

        button.className =
        'navBtn';

        button.innerText =
        scene.title;

        if(index===0){

            button.classList.add(
                'active'
            );

            updateTitle(
                scene.title
            );

        }

        button.onclick = ()=>{

            loadScene(
                scene.id
            );

            updateTitle(
                scene.title
            );

            document
            .querySelectorAll(
                '.navBtn'
            )
            .forEach(btn=>{

                btn.classList.remove(
                    'active'
                );

            });

            button.classList.add(
                'active'
            );

        };

        bottomNav.appendChild(
            button
        );

    });

}