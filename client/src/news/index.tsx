import React, {
  useCallback,
  useContext,
  useEffect,
  useReducer,
  useState,
} from "react";
import styled from "styled-components";

import NewsContext, { NewsProvider } from "./context";
import NewsArticles from "./articles";
import NewsWords from "./words";

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

const Button = styled.div`
  cursor: pointer;
  border-radius: 0.5rem;
  background-color: #2d848a;
  color: white;
  width: auto;
  box-sizing: border-box;
  padding: 0.5rem 1rem;
`;

const URL = styled.a`
  text-decoration: none;
  color: white;
`;

const FetchNewsFeed = styled(Button)`
  margin-left: auto;
`;

const token = "7dd941adac8141a3a12db7ff602f712d";

const Input = styled.input`
  border-radius: 0.5rem;
  padding: 0.5rem;
`;

export const NewsAnalyzerHeader = () => {
  const [{ access_token, amount }, dispatch] = useContext(NewsContext);

  const onInput = (val: any) =>
    dispatch({ type: "SET_TOKEN", payload: val.target.value });

  const getNews = useCallback(async () => {
    const resp = await fetch(`/news?token=${access_token}&amount=${amount}`, {
      method: "get",
    });
    const result = await resp.json();

    dispatch({ type: "SET_ARTICLES", payload: result.articles });
    dispatch({ type: "SET_WORDS", payload: result.stats });
  }, [dispatch, access_token, amount]);

  return (
    <RefreshPanel>
      <Button>
        <URL target="_blank" href="https://newsapi.org/account">
          Acquire API Token
        </URL>
      </Button>
      <Input placeholder="Provided token" onChange={onInput}></Input>
      <FetchNewsFeed onClick={getNews}>Fetch News</FetchNewsFeed>
    </RefreshPanel>
  );
};

export const NewsAnalyzer = () => {
  return (
    <NewsProvider>
      <Box>
        <NewsAnalyzerHeader />
        <NewsWords />
        <NewsArticles />
      </Box>
    </NewsProvider>
  );
};

export default NewsAnalyzer;
