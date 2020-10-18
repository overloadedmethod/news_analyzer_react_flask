import React, {
  useCallback,
  useContext,
  useEffect,
  useReducer,
  useState,
} from "react";
import styled from "styled-components";

import NewsContext from "./context";
import NewsArticles from "./articles";
import NewsWords from "./words";
import Days from "./days";

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

  const fetchDays = useCallback(async () => {
    const resp = await fetch(`/fetch_days?token=${access_token}`, {
      method: "get",
    });
    const result = await resp.json();
    if (result.length) {
      dispatch({ type: "SET_DAYS_AGGREGATION", payload: result });
      return;
    }

    await new Promise((resolve) => setTimeout(resolve, 5000));

    const snd_try = await fetch(`/fetch_days?token=${access_token}`, {
      method: "get",
    });
    const res = await snd_try.json();
    dispatch({ type: "SET_DAYS_AGGREGATION", payload: res });
  }, [dispatch, access_token]);

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
      <FetchNewsFeed onClick={getNews(7, 100)}>Fetch Last 100</FetchNewsFeed>

      <FetchNewsFeed onClick={fetchDays}>Show loaded 7 days</FetchNewsFeed>
    </RefreshPanel>
  );
};

export const NewsAnalyzer = () => {
  const [{ articles, words, days_aggregation }] = useContext(NewsContext);

  return (
    <Box>
      <NewsAnalyzerHeader />
      {!!days_aggregation.length && <Days />}
      <NewsWords words={words} />
      <NewsArticles articles={articles} />
    </Box>
  );
};

export default NewsAnalyzer;
