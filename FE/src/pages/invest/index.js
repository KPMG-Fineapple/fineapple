import { Box, Grid, ThemeProvider, createTheme } from "@mui/material";
import Typography from "@mui/material/Typography";
import { Layout } from "src/components/home/layout";
import Card from "src/components/invest/card";

const theme = createTheme({
  palette: {
    primary: {
      main: "#00c4c4",
      contrastText: "#fff",
    },
  },
});

function investDashboard(props) {
  const { items } = props;
  return (
    <ThemeProvider theme={theme}>
      <Box
        sx={{
          marginTop: 10,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Box sx={{ marginBottom: 8 }}>
          <Typography component="h1" variant="h4">
            관심 있는 발전소를 선택해주세요
          </Typography>
        </Box>

        <Grid container spacing={3} columns={27} sx={{ maxWidth: 3000 }}>
          {items.map((item) => (
            <Grid item xs={9}>
              <Card
                imgURL={`${item.imageUrl}?w=164&h=164&fit=crop&auto=format`}
                srcSet={`${item.imageUrl}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                alt={item.title}
                title={item.title}
                totalFund={item.totalFund}
                profitPercent={item.profitPercent}
                fundingPercent={item.fundingPercent}
                id={item.id}
              />
            </Grid>
          ))}
        </Grid>
      </Box>
    </ThemeProvider>
  );
}

investDashboard.getLayout = (page) => <Layout>{page}</Layout>;

export default investDashboard;

export async function getServerSideProps() {
  const items = await (
    await fetch("http://localhost:3001/api/invest/items")
  ).json();

  return {
    props: {
      items,
    },
  };
}
