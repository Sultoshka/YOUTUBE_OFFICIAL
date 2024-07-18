const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

app.get('/videos', (req, res) => {
    const videos = [
        { id: 1, title: 'Video 1', url: 'http://example.com/video1.mp4' },
        { id: 2, title: 'Video 2', url: 'http://example.com/video2.mp4' },
    ];
    res.json(videos);
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});