function initializeBranding(){

    const logo =
    document.getElementById(
        'triptLogo'
    );

    if(!logo) return;

    logo.addEventListener(
        'click',
        ()=>{

            window.open(
                'https://tript.in',
                '_blank'
            );

        }
    );

}