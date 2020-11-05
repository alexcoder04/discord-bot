
const Discord = require("discord.js");
//const readline = require("readline");
const fs = require("fs");

const NAME = "Erhardt";
const GENERAL_CHANNEL_ID = "XXX";
const ATTACHMENT_URL = "XXX";
const ADMIN_PWD = "...";

const client = new Discord.Client();

client.on("ready", () => {
  printMessage("LOGIN", "Logged in as " + client.user.tag);

  //client.user.setActivity("JS", {type: "PLAYING"});

  console.log("logged in on following channels:");
  client.guilds.forEach(guild => {
    guild.channels.forEach(channel => {
      console.log("guild: ${guild.name} - channel - ${channel.type} : ${channel.id}");
    });

  });

  const generalChannel = client.channels.get(GENERAL_CHANNEL_ID);
  //const attachment = new Discord.Attachment(ATTACHMENT_URL)
  generalChannel.send("Hey, I'm online!");
});

client.on("message", (message) => {
  // ignoring own messages
  if (message.author == client.user) return
  //msg.channel.send("I received your message: " + msg.content);

  if (message.content.toLowerCase().includes(NAME.toLowerCase())){
    // analyse message
    if (message.content == `$sudo %${ADMIN_PWD} shutdown`){
      process.exit(0);
    }
  }
});

function printMessage(key, message){
  console.log(`[TIME] [${key}] ${message}`);
}

fs.readFile("../secret.json", "utf8", (err, data) => {
  if (err){
    printMessage("ERROR", err)
  } else {
    client.login(JSON.parse(data).token);
  }
});
