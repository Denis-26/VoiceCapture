var a;

navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();

        const audioChunks = [];
        mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
        });

        mediaRecorder.addEventListener("stop", () => {
              const audioBlob = new Blob(audioChunks);
              const audioUrl = URL.createObjectURL(audioBlob);
              const audio = new Audio(audioUrl);
              audioBlob.arrayBuffer()
                .then((buffer) => {
                    console.log(buffer);
                    a = new Int8Array(buffer);
                    console.log(a);
                });
              audio.play();
        });

        setTimeout(() => {
            mediaRecorder.stop();
        }, 3000);
});