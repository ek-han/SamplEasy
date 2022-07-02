import request from "@/api/http";

export const receiveMessages = () => {
  const query = {
    method: "GET",
    url: "http://localhost:8000/getAllMessages",
  };

  return request(query).then((data) => {
    return data;
  });
};
