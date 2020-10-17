import React, { useContext } from "react";
import styled from "styled-components";
import NewsContext from "./context";

const ArticlesBox = styled.div`
  background-color: #d6edff;
`;

const Article = styled.div`
  padding: 1rem;
  margin: 1rem;
`;

const ArticleTitle = styled.div`
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
`;

const ArticleDescription = styled.div`
  margin-top: 0.5rem;
  font-size: 1rem;
`;

export const Articles = () => {
  const [{ articles }] = useContext(NewsContext);

  return (
    <ArticlesBox>
      {articles.map(({ title, description }: any, index) => (
        <Article key={index}>
          <ArticleTitle>{title}</ArticleTitle>
          <ArticleDescription>{description}</ArticleDescription>
        </Article>
      ))}
    </ArticlesBox>
  );
};

export default Articles;
