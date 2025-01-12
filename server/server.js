const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const sgMail = require("@sendgrid/mail");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Set the SendGrid API key
sgMail.setApiKey(process.env.SANDGRID_API);

// Route to handle contact form submissions
app.post("/send-email", async (req, res) => {
    const { name, bname, email, phone, message } = req.body;

    const msg = {
        to: "support@iveew.co", // Replace with the email address you want to receive messages
        from: "support@iveew.co", // Replace with a verified sender email in SendGrid
        subject: `New Contact Form Submission from ${name}`,
        text: `
            Name: ${name}
            Business Name: ${bname}
            Email: ${email}
            Phone: ${phone}
            Message: ${message}
        `,
        html: `
            <p><strong>Name:</strong> ${name}</p>
            <p><strong>Business Name:</strong> ${bname}</p>
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Phone:</strong> ${phone}</p>
            <p><strong>Message:</strong></p>
            <p>${message}</p>
        `,
    };

    try {
        await sgMail.send(msg);
        res.status(200).send({ success: true, message: "Email sent successfully!" });
    } catch (error) {
        console.error(error);
        res.status(500).send({ success: false, message: "Failed to send email." });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
