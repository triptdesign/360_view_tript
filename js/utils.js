function validateScenes(){

    if(
        typeof window.PANORAMA_SCENES
        === 'undefined'
    ){

        alert(
            "scenes.js not found.\n\nRun generate_scenes.py first."
        );

        throw new Error(
            "scenes.js missing"
        );

    }

}
