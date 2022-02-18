import { Box } from "@mui/material";
import { ThemeProvider } from "@mui/styles";
import { Container, createTheme, CssBaseline } from "@mui/material";
import Header from "src/components/home/header";

export const Layout = (props) => {
  const { children } = props;
  const theme = createTheme();

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg" sx={{ mb: "100px" }}>
        <Header title="Fine apple" sections={[]} />
        {children}
      </Container>
    </ThemeProvider>
  );
};
