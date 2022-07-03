import request from "@/api/http";

export const loadGenreSeeds = ({ commit }) => {
  const query = {
    method: "GET",
    url: "https://api.spotify.com/v1/recommendations/available-genre-seeds",
  };

  return request(query).then((data) => {
    commit("SetGenreSeeds", data.genres);
  });
};
