import React, { useEffect, useState } from "react";
import styled from "styled-components";

const Box = styled.div`
  background-color: #f7fff7;
  width: 100%;
  height: 100%;
`;

const RefreshPanel = styled.div`
  display: inline-flex;

  background-color: #c1dff0;
  width: 100%;
  height: auto;
  padding: 0.5rem 1rem;
  & > * {
    margin: 0.5rem 1rem;
  }
`;

const FetchNewsFeed = styled.div`
  border-radius: 0.5rem;
  background-color: #2d848a;
  color: white;
  /* height: 1.5rem; */
  width: auto;
  box-sizing: border-box;
  padding: 0.5rem 1rem;
  margin-left: auto;
`;

const token = "7dd941adac8141a3a12db7ff602f712d";

const newsAPI = `http://newsapi.org/v2/everything?language=en&pageSize=5&sortBy=published
At&sources=bbc-news&apiKey=${token}
`;

// async function fetchNews() {
//   const val = await fetch(newsAPI, {
//     method: "get",
//   }).then((resp) => resp.json());
//   return val;
// }

export const NewsAnalyzer = () => {
  const [news, setNews] = useState();

  // useEffect(() => {
  //   fetchNews().then(setNews);
  // }, []);

  return (
    <Box>
      <RefreshPanel>
        <FetchNewsFeed>Fetch News</FetchNewsFeed>
      </RefreshPanel>
    </Box>
  );
};

export default NewsAnalyzer;
