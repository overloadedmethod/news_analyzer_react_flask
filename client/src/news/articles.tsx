import React, { useContext } from "react";
import styled from "styled-components";
import NewsContext from "./context";

const ArticlesBox = styled.div``;

export const Articles = () => {
  const [{ articles }] = useContext(NewsContext);

  return <ArticlesBox>{articles.map((article) => article)}</ArticlesBox>;
};
