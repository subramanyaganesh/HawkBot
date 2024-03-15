// in config.js
import { createChatBotMessage } from "react-chatbot-kit";
import Avatar from "@mui/material/Avatar";
import BotChatBox from "../Components/BotChatBox";
import UserChatBox from "../Components/UserChatBox";

const botName = "HawkBot";

const config = {
  initialMessages: [
    createChatBotMessage({
      answer: `Hello! I'm ${botName}, your personal assistant`,
      sources: [
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://www.iit.edu/registrar/academic-calendar",
      ],
    }),
  ],
  botName: botName,
  customComponents: {
    header: () => (
      <div className="chatbot-header">
        <Avatar
          alt="Hawk Bot"
          sx={{ display: "inline-block", margin: "8px" }}
          src={require("../assets/hawk_image.jpg")}
        />{" "}
        HawkBot
      </div>
    ),
    botAvatar: (props) => (
      <Avatar
        alt="Hawk Bot"
        src={require("../assets/hawk_image.jpg")}
        {...props}
      />
    ),
    botChatMessage: (props) => <BotChatBox {...props} />,
    userChatMessage: (props) => <UserChatBox {...props} />,
    userAvatar: (props) => null,
  },
  customStyles: {
    botMessageBox: {
      backgroundColor: "#376B7E",
    },
    chatButton: {
      backgroundColor: "#D71313",
    },
  },
};

export default config;
