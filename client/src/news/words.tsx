import React, { useContext } from "react";
import styled from "styled-components";
import NewsContext from "./context";

const WordsBox = styled.div``;

export const Words = () => {
  const [{ words }] = useContext(NewsContext);

  return (
    <WordsBox>{Object.entries(words).map((word, amount) => word)}</WordsBox>
  );
};
