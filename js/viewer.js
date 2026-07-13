let viewer;

let scenes = {};

function buildScenes(){

    scenes = {};

    window.PANORAMA_SCENES
    .forEach(scene=>{

        scenes[scene.id] = {

            //title:scene.title,

            type:'equirectangular',

            panorama:
            'assets/panoramas/' +
            scene.file

        };

    });

}

function createViewer(){

    const firstScene =
    window.PANORAMA_SCENES[0].id;

    viewer =
    pannellum.viewer(
        'panorama',
        {

            default:{

                firstScene:firstScene,

                autoLoad:true,

                sceneFadeDuration:1000

            },

            scenes:scenes

        }
    );

}

function loadScene(sceneId){

    viewer.loadScene(
        sceneId
    );

}