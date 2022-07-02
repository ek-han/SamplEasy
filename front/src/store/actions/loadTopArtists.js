import request from "@/api/http";

export const loadTopArtists = () => {
  const query = {
    method: "GET",
    url: "https://api.spotify.com/v1/me/top/artists?time_range=medium_term&limit=10&offset=5",
  };

  return request(query).then((data) => {
    console.log("Data:", data);
  });
};
