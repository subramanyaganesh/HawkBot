// in ActionProvider.jsx
import React from "react";
import axios from "axios";

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  // const api = "http://localhost:8000/api/getAnswer/";
  // const api = "https://192.168.147.35:8000/api/getAnswer/";
  const api = "https://hawkbot-tenant.iit.edu:8000/api/getAnswer/";

  const handleHello = () => {
    const botMessage = createChatBotMessage(
      {
        answer: "Hello. how can I help you today?.",
        sources: [],
      },
      {
        delay: 1000,
      }
    );

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };

  let apiCallQueue = Promise.resolve();

  const clientMessage = async (clientMessage) => {
    const currentCall = async () => {
      try {
        addMessageToState(clientMessage);
        const data = clientMessage;
        greet({ answer: "Loading", sources: [] });
        const apiResp = await axios.post(api, data);

        if (apiResp.status === 200) {
          greet(apiResp.data, true);
        } else {
          greet({ answer: "Fetch Failed", sources: [] }, true);
        }
      } catch (error) {
        greet({ answer: "Fetch Failed", sources: [] }, true);
      }
    };
    apiCallQueue = apiCallQueue.then(currentCall).catch(console.error);
  };

  // const clientMessage = async (clientMessage) => {
  //   addMessageToState(clientMessage);
  //   const data = clientMessage;
  //   try {
  //     greet({ answer: "Loading", sources: [] });
  //     const apiResp = await axios.post(api, data);
  //     if (apiResp.status === 200) {
  //       greet(apiResp?.data, true);
  //     } else {
  //       greet({ answer: "Fetch Failed", sources: [] }, true);
  //     }
  //   } catch {
  //     greet({ answer: "Fetch Failed", sources: [] }, true);
  //   }
  // };

  const removeLoadingMessage = (prevstateArray, removeLoading) => {
    if (removeLoading) {
      prevstateArray?.messages?.splice(
        prevstateArray?.messages?.findIndex(
          // (a) => a?.message?.message.answer === "Loading"
          (a) => {
            return a?.message?.answer === "Loading";
          }
        ),
        1
      );
      return prevstateArray;
    } else {
      return prevstateArray;
    }
  };

  const addMessageToState = (message, removeLoading = false) => {
    setState((prevstate) => ({
      ...removeLoadingMessage(prevstate, removeLoading),
      messages: [...prevstate.messages, message],
    }));
  };

  const greet = (botMessage, removeLoading = false) => {
    const message = createChatBotMessage(botMessage, {
      delay: 500,
    });
    addMessageToState(message, removeLoading);
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleHello,
            clientMessage,
          },
        });
      })}
    </div>
  );
};

export default ActionProvider;
