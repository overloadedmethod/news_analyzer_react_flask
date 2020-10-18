import React, { useContext } from "react";
import styled from "styled-components";
import NewsContext from "./context";

const WordsBox = styled.div`
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: start;
  align-items: auto;
  align-content: start;
`;

const WordBox = styled.div`
  margin: 1rem;
  box-shadow: -1px 3px 12px 1px rgba(143, 180, 186, 1);
`;

const Word = styled.span`
  background-color: #acd7ec;
  border-radius: 0.5rem 0 0 0.5rem;
  padding: 0.5rem;
`;

const Amount = styled.span`
  border-radius: 0 0.5rem 0.5rem 0;
  background-color: #84dcc6;
  height: 100%;
  padding: 0.5rem;
`;

export const Words = ({ words = {} }: { words: Record<string, number> }) => {
  return (
    <WordsBox>
      {Object.entries(words).map(([word, amount]) => (
        <WordBox key={word}>
          <Word>{word}</Word>
          <Amount>{amount}</Amount>
        </WordBox>
      ))}
    </WordsBox>
  );
};

export default Words;
