const express = require('express');
const app = express();
const port = 3000;

// Serve static files from the project directory
app.use(express.static(__dirname));

// Handle the crypto reward request
app.post('/reward-crypto', express.json(), (req, res) => {
    const { user, receiverAddress, amount } = req.body;
    console.log(`Rewarding ${amount} crypto to ${user} at address ${receiverAddress}`);
    res.json({ success: true, message: ${amount} crypto sent to ${receiverAddress} });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
