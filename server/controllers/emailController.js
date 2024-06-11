import nodemailer from "nodemailer";
import "../loadEnvironment.js";

export async function sendEmail(req, res) {
  const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      type: "OAuth2",
      user: process.env.GMAIL_USER,
      pass: process.env.GMAIL_PASS,
      clientId: process.env.GMAIL_CLIENT_ID,
      clientSecret: process.env.GMAIL_SECRET_CLIENT,
      refreshToken: process.env.GMAIL_REFRESH_TOKEN,
    },
  });

  try {
    const mailOptions = {
      from: { name: req.body.displayName, email: req.body.email }, // Doesn't show this from name attribute on the actual email
      to: process.env.GMAIL_RECIPIENT,
      subject: "Nuevo mensaje desde nescomrd.com",
      text: req.body.message,
    };

    transporter.sendMail(mailOptions, async function (err, data) {
      if (err) {
        res.status(500).json({ message: err.message });
      } else {
        res.send("Email sent successfully").status(200);
      }
    });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}
