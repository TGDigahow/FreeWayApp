document.getElementById('load-route-btn').addEventListener('click', function () {
    const options = document.getElementById('options');
    const selectedOption = options.value;
    const accessibilitySwitch = document.getElementById('accessibility-switch').checked;
    const miniplayerContainer = document.getElementById('miniplayer-container');

    let accessibilityText = accessibilitySwitch ? "com acessibilidade" : "sem acessibilidade";
    let imageSrc = "";

    // Definir imagens com base na seleção e acessibilidade
    switch (selectedOption) {
        case "Biblioteca":
            imageSrc = accessibilitySwitch ? "A:/mapa2.gif" : "A:/mapa6.gif";
            break;
        case "Financeiro":
            imageSrc = accessibilitySwitch ? "A:/mapa3.gif" : "A:/mapa7.gif";
            break;
        case "Secretaria":
            imageSrc = accessibilitySwitch ? "A:/mapa1.png" : "A:/mapappagaio.gif";
            break;
        case "Sala 2.3":
            imageSrc = accessibilitySwitch ? "A:/mapa5.gif" : "A:/escada.gif";
            break;
        default:
            imageSrc = "";
    }

    // Atualizar conteúdo do container
    miniplayerContainer.innerHTML = `
        <p>Destino: ${selectedOption} (${accessibilityText})</p>
        <img src="${imageSrc}" alt="Rota" class="route-image">
    `;
});
