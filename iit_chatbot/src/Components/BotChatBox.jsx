import React from "react";
import { Bars } from "react-loader-spinner";

export default function BotChatBox(props) {
  console.log(props.message);
  return (
    <div>
      <div className="chatbot-bot-message">
        {props.message.answer === "Loading" ? (
          <Bars
            height="25"
            width="25"
            color="#D71313"
            ariaLabel="bars-loading"
            wrapperStyle={{}}
            wrapperClass=""
            visible={true}
          />
        ) : (
          props.message.answer
        )}
      </div>
      {props.message.sources.map((source) => {
        return (
          <>
            <div className="spacing-sources"></div>
            <p className="source-para">
              <a className="para-link" href={source}>
                {source.slice(0, 40) + "..."}
              </a>
            </p>
          </>
        );
      })}
    </div>
  );
}
