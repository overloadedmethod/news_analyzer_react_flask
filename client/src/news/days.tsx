import React, { useContext } from "react";
import styled from "styled-components";
import NewsContext from "./context";
import Words from "./words";

const Box = styled.div``;

const Day = styled.div`
  box-sizing: border-box;
  padding: 1rem;
`;

export const Days = () => {
  const [{ days_aggregation }] = useContext(NewsContext);

  return (
    <Box>
      {days_aggregation.map(({ stats }) => (
        <Day>
          <Words words={stats} />
        </Day>
      ))}
    </Box>
  );
};

export default Days;
