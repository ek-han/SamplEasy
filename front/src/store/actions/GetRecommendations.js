import request from "@/api/http";

export const GetRecommendations = ({ getters, commit }) => {
  const selectedGenres = getters["selectedGenres"];
  const genres = selectedGenres.join(",");
  const query = {
    method: "GET",
    url: `https://api.spotify.com/v1/recommendations?seed_genres=${genres}`,
  };

  return request(query).then((data) => {
    const dataFormatted = data.tracks.map((t) => {
      return {
        id: t.id,
        uri: t.uri,
        name: t.name,
        popularity: t.popularity,
        mainArtist: t.artists[0].name,
      };
    });
    commit("setRecommendations", dataFormatted);
  });
};
