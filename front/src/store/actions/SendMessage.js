import request from "@/api/http";

export const sendMessage = (store, payload) => {
  const query = {
    method: "POST",
    url: "http://localhost:8000/send_message",
    data: {
      msg: payload.msg,
    },
  };

  return request(query).then((data) => {
    console.log("DATA:", data);
  });
};
