const oscuridad = document.getElementById('oscuridad');

document.addEventListener('mousemove', (e) => {
    const x = e.clientX;
    const y = e.clientY;

    oscuridad.style.background = `radial-gradient(circle 120px at ${x}px ${y}px, transparent 0%, rgba(0,0,0,0.95) 100%)`;
});