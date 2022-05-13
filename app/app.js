import express from "express";
import { execSync } from "child_process";
const app = express();
const port = process.env.PORT;
var HttpStatusCode;
(function (HttpStatusCode) {
    HttpStatusCode[HttpStatusCode["OK"] = 200] = "OK";
})(HttpStatusCode || (HttpStatusCode = {}));
app.get("/", (req, res) => {
    let result = execSync("hostname -i");
    let ip = result.toString("utf-8").replace("\n\n", "").trim();
    res.status(HttpStatusCode.OK).send({
        status: "ok",
        statusCode: 200,
        containerIP: ip,
        message: `Hello world from container ${ip.split(".")[3]}!`,
    });
});
app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
