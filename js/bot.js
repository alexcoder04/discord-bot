
const discord = require("discord.js");
const fs = require("fs");

const NAME = "Erhardt";
const GENERAL_CHANNEL_ID = "XXX";
const ATTACHMENT_URL = "XXX";
const ADMIN_PWD = "...";

class JSDiscordBot extends discord.Client {
  constructor() {
    this.readConfig();
  }

  readConfig(){
    fs.readFile("../config.json", "utf8", (err, data) => {
      if (err) {
        this.printMessage("error", err);
      } else {
        that.config = JSON.parse(data);
      }
    });
  }

  printMessage(key, message){
    console.log(`[${new Date().now().toLocaleTimeString()}] [${key.toUpperCase()}] ${message}`);
  }

  run(){
    fs.readFile("../secret.json", "utf8", (err, data) => {
      if (err){
        printMessage("error", err)
      } else {
        that.login(JSON.parse(data).token);
      }
    });
  }
}

const client = new JSDiscordBot();

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
    if (message.content.includes("$sudo") && message.content.includes("%" + ADMIN_PWD) && message.content.includes("shutdown"){
      process.exit(0);
    }
  }
});

client.run();
