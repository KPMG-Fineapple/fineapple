import { styled } from "@mui/material/styles";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import ButtonBase from "@mui/material/ButtonBase";
import Stack from "@mui/material/Stack";
import { useRouter } from "next/router";

const Img = styled("img")({
  margin: "auto",
  display: "block",
  maxWidth: "100%",
  maxHeight: "100%",
});

export default function Card({ imgURL, title, description, id }) {
  const router = useRouter();

  return (
    <Paper
      sx={{
        p: 2,
        margin: "auto",
        maxWidth: 700,
        flexGrow: 1,
      }}
    >
      <Grid container spacing={2}>
        <Stack spacing={0} sx={{ marginLeft: 2 }}>
          <ButtonBase sx={{ width: 150, height: 180 }}>
            <Img alt="complex" src={imgURL} />
          </ButtonBase>
        </Stack>
        <Grid item xs={12} sm container sx={{ marginTop: 4 }}>
          <Grid item xs container direction="column" spacing={2}>
            <Grid item xs>
              <Typography gutterBottom variant="subtitle1" component="div">
                {title}
              </Typography>
              <Typography variant="body2" gutterBottom>
                {description}
              </Typography>
            </Grid>
            <Grid item sx={{ marginLeft: 4 }}>
              <Button
                onClick={() => router.push(`/invest/items/${id}`)}
                variant="contained"
                sx={{ padding: 1 }}
              >
                자세히 알아보기{" "}
              </Button>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Paper>
  );
}
