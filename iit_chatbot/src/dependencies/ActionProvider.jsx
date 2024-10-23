// in ActionProvider.jsx
import React from 'react';
import axios from "axios";

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleHello = () => {
    const botMessage = createChatBotMessage('Hello. Nice to meet you.',{
        delay:1000,
    });

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };

  const clientMessage = async (clientMessage) => {
    addMessageToState(clientMessage);
    const data = clientMessage
    try {
      greet("Loading" );    // I am using message object, you can use string too
      const apiResp = await axios.post("http://localhost:8000/api/getAnswer/",data);//"https://random-word-api.herokuapp.com/word"
      if (apiResp.status == 200) {
        greet(apiResp?.data.answer, true);    // Sending true as second parameter as  i need to stop loading that chat object response once API call is finished. Will discuss it further in next steps
      } else {
        greet('FAIL_TO_ANSWER',true);
      }
    } catch {
      greet('FAIL_TO_ANSWER',true);
    }
  };

  const removeLoadingMessage = (prevstateArray, removeLoading) => {
    if (removeLoading) {
      prevstateArray?.messages?.splice(
        prevstateArray?.messages?.findIndex(
          (a) => a?.message?.message === "Loading"
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
    const message = createChatBotMessage(botMessage,{
        delay:500,
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