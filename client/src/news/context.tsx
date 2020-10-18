import React, { createContext, useReducer } from "react";

const initialState = {
  articles: [] as {
    title: string;
    details: string;
  }[],
  words: {} as Record<string, number>,
  access_token: "" as string,
  amount: 5,
};

type NewsActions = "SET_ARTICLES" | "SET_WORDS" | "SET_TOKEN" | "SET_AMOUNT";

const actions: Record<
  string,
  (prev: typeof initialState, change: any) => typeof initialState
> = {
  SET_ARTICLES: (prev, articles) => ({ ...prev, articles }),
  SET_WORDS: (prev, words) => ({ ...prev, words }),
  SET_TOKEN: (prev, access_token) => ({ ...prev, access_token }),
  SET_AMOUNT: (prev, amount) => ({ ...prev, amount }),
};

const reducer = (
  state = initialState,
  { type, payload }: { type: string; payload: any }
) => {
  return actions[type]?.(state, payload) ?? state;
};

const NewsContext = createContext([initialState, console.info] as [
  typeof initialState,
  (action: { type: NewsActions; payload: any }) => void
]);

export const NewsProvider = ({ children }: { children: any }) => {
  const [store, dispatch] = useReducer(reducer, initialState);

  return (
    <NewsContext.Provider value={[store, dispatch]}>
      {children}
    </NewsContext.Provider>
  );
};

export default NewsContext;
