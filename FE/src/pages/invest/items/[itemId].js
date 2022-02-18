import { Layout } from "src/components/home/layout";
import { ItemImage } from "src/components/invest/image";
import {
  Box,
  Container,
  Grid,
  Typography,
  Divider,
  Button,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from "@mui/material";
import { InvestInfoBar } from "src/components/invest/invest-info-bar";
import { InvestAccordions } from "src/components/invest/accordion";
import { Chart } from "src/components/dashboard/chart";
import { CompanyCard } from "src/components/invest/company";

const theme = createTheme({
  palette: {
    primary: {
      main: "#00c4c4",
      contrastText: "#fff",
    },
  },
});
function Item({ item, powerGenrationResult }) {
  const { companyInfo } = item;

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth={false}>
        <Grid container spacing={8}>
          <Grid item lg={6} md={6} xl={6} xs={12}>
            <ItemImage path={item.imageUrl} width={560} height={440} />
          </Grid>
          <Grid item lg={6} md={6} xl={6} xs={12}>
            <Box>
              <Typography align="left" variant="h5">
                {item.title}
              </Typography>
              <Box
                sx={{
                  justifyContent: "space-between",
                  display: "flex",
                  mt: "15px",
                }}
              >
                <Typography align="center" variant="subtitle2">
                  {item.investorNumber.toLocaleString("ko-KR")}명 참여
                </Typography>
                <Typography align="center" variant="h6" color="primary">
                  {item.price.toLocaleString("ko-KR")}원
                </Typography>
              </Box>
              <Divider
                sx={{
                  borderColor: "#2D3748",
                  mt: 3,
                  mb: 6,
                }}
              />
              <Button
                variant="contained"
                fullWidth={true}
                sx={{ fontSize: "20px", mb: "40px" }}
              >
                펀딩하기
              </Button>
              <Box>
                <Typography align="left" variant="subtitle2">
                  현재 투자 정보
                </Typography>
                <InvestInfoBar
                  title="진행 중인 투자 금액"
                  value={`${item.investAmount.toLocaleString("ko-KR")}원`}
                />
                <InvestInfoBar
                  title="투자자 수"
                  value={`${item.investorNumber.toLocaleString("ko-KR")}명`}
                />
              </Box>
            </Box>
          </Grid>
          <Grid item lg={6} md={6} xl={6} xs={12}>
            <InvestAccordions
              title="더 많은 투자 정보"
              items={["생산성", "투자 방식"]}
            />
          </Grid>
          <Grid item lg={6} md={6} xl={6} xs={12}>
            <CompanyCard companyInfo={companyInfo} />
          </Grid>
          <Grid item lg={6} md={6} xl={6} xs={12}>
            <Chart
              title="현재 발전량"
              allowtoggle="off"
              result={powerGenrationResult}
            />
          </Grid>
          <Grid item lg={6} md={6} xl={6} xs={12}>
            <Chart title="예상 수익률" allowtoggle="off" result={item.yield} />
          </Grid>
        </Grid>
      </Container>
    </ThemeProvider>
  );
}

Item.getLayout = (page) => <Layout>{page}</Layout>;

export default Item;

const createCurrentGenration = (powerGenration) => {
  return powerGenration.map((item, idx) => {
    const { date } = item;
    return {
      name: `${date.substring(5, date.length)}월`,
      발전량: powerGenration[idx].value.reduce((acc, cur) => acc + cur),
    };
  });
};

export async function getServerSideProps({ params: { itemId } }) {
  const item = await (
    await fetch(`http://localhost:3001/api/invest/items/${itemId}`)
  ).json();

  const powerGenrationResult = await (
    await fetch(`http://localhost:3001/api/predict/power-generation`)
  ).json();

  return {
    props: {
      item,
      powerGenrationResult: createCurrentGenration(
        powerGenrationResult.current
      ),
    },
  };
}
