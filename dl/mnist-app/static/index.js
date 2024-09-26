document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    let isDrawing = false;

    // Set up canvas for drawing
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 15;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    // Drawing functions
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);

    // Touch support for mobile devices
    canvas.addEventListener('touchstart', handleTouch);
    canvas.addEventListener('touchmove', handleTouch);
    canvas.addEventListener('touchend', stopDrawing);

    function startDrawing(e) {
        isDrawing = true;
        draw(e);
    }

    function draw(e) {
        if (!isDrawing) return;

        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x, y);
    }

    function stopDrawing() {
        isDrawing = false;
        ctx.beginPath();
    }

    function handleTouch(e) {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousemove', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    }

    // Clear canvas
    document.getElementById('clearBtn').addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    // Predict
    document.getElementById('predictBtn').addEventListener('click', () => {
        // Get the full image data from the canvas
        const imageData = canvas.toDataURL('image/png');
        // Create a blob from the image data
        const blob = dataURItoBlob(imageData);
        // Send the full image data to the server
        const formData = new FormData();
        formData.append('image', blob, 'drawing.png');
        // Helper function to convert data URI to Blob
        function dataURItoBlob(dataURI) {
            const byteString = atob(dataURI.split(',')[1]);
            const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            return new Blob([ab], {type: mimeString});
        }
        fetch('/predict', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(result => {
            document.getElementById('result').innerHTML = result.prediction;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
