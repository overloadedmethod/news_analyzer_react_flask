import React, { useEffect, useState } from "react";
import styled from "styled-components";
import Example from "./example";

const Box = styled.div`
  background-color: #f7fff7;
  width: 100%;
  height: 100%;
`;

const RefreshPanel = styled.div`
  display: inline-flex;
  background-color: #c1dff0;
  width: 100%;
  box-sizing: border-box;
  height: auto;
  padding: 0.5rem 0rem;
  & > * {
    margin: 0.5rem 1rem;
  }
`;

const FetchNewsFeed = styled.div`
  cursor: pointer;
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

export const NewsAnalyzer = () => {
  const [news, setNews] = useState();
  const example = Example;
  return (
    <Box>
      <RefreshPanel>
        <FetchNewsFeed>Fetch News</FetchNewsFeed>
      </RefreshPanel>
    </Box>
  );
};

export default NewsAnalyzer;
