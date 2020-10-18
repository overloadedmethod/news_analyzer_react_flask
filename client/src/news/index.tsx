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

const Input = styled.input`
  border-radius: 0.5rem;
  padding: 0.5rem;
`;

export const NewsAnalyzerHeader = () => {
  const [{ access_token, amount, days }, dispatch] = useContext(NewsContext);

  const onTokenChange = (val: any) =>
    dispatch({ type: "SET_TOKEN", payload: val.target.value });

  const onAmountChange = (val: any) =>
    dispatch({ type: "SET_AMOUNT", payload: val.target.value });

  const onDaysChange = (val: any) =>
    dispatch({ type: "SET_DAYS", payload: val.target.value });

  const getNews = useCallback(
    (days: number, amount: number) => async () => {
      const resp = await fetch(
        `/news?token=${access_token}&amount=${amount}&days=${days}`,
        {
          method: "get",
        }
      );
      const result = await resp.json();

      dispatch({ type: "SET_ARTICLES", payload: result.articles });
      dispatch({ type: "SET_WORDS", payload: result.stats });
    },
    [dispatch, access_token, amount, days]
  );

  return (
    <RefreshPanel>
      <Button>
        <URL target="_blank" href="https://newsapi.org/account">
          Acquire API Token
        </URL>
      </Button>
      <Input placeholder="Provided token" onChange={onTokenChange}></Input>
      <Input
        onChange={onAmountChange}
        placeholder="amount"
        value={amount}
        type="number"
        min={1}
        max={500}></Input>
      <Input
        onChange={onDaysChange}
        placeholder="days"
        value={days}
        type="number"
        min={1}
        max={500}></Input>
      <FetchNewsFeed onClick={getNews(days, amount)}>
        Fetch explicit amount and days
      </FetchNewsFeed>
      <FetchNewsFeed onClick={getNews(-1, 100)}>Fetch Last 100</FetchNewsFeed>
      <FetchNewsFeed onClick={getNews(7, -1)}>Fetch Last 7 days</FetchNewsFeed>
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
