import { ClearAllRounded, Settings } from "@mui/icons-material";
import { LoadingButton } from "@mui/lab";
import {
  Box,
  Button,
  Grid,
  MenuItem,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import axios from "axios";
import LoadingScreen from "components/LoadingScreen";
import React, { useState } from "react";
import { toast } from "react-toastify";

const Home: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [data, setData] = useState({
    Sex: 1,
    Length: 0.36,
    Diameter: 0.285,
    Height: 0.105,
    "Whole weight": 0.2415,
    "Shucked weight": 0.0915,
    "Viscera weight": 0.057,
    "Shell weight": 0.075,
  });
  const onChangeDataHandler = (field: string, value: string) => {
    setData({ ...data, [field]: value });
  };
  const predictHandler = async () => {
    setLoading(true);
    try {
      const res = await axios.post("/predict-age", data);
      setResult(res.data.age);
      document.getElementById("slide-to-result").click();
      toast.success("Prediction successful");
    } catch (error) {
      toast.error(error.message);
    }
    setLoading(false);
  };

  const clearHandler = () => {
    setResult(null);
    setData({
      Sex: 1,
      Length: 0,
      Diameter: 0,
      Height: 0,
      "Whole weight": 0,
      "Shucked weight": 0,
      "Viscera weight": 0,
      "Shell weight": 0,
    });
  };

  return (
    <Paper
      elevation={6}
      sx={{
        p: 3,
        maxWidth: "md",
        maxHeight: "100vh",
        overflow: "auto",
        position: "fixed",
        top: { xs: 0, md: "50%" },
        left: { xs: 0, md: "50%" },
        transform: { xs: 0, md: "translate(-50%,-50%)" },
        zIndex: 0,
        height: { xs: "100vh", md: "auto" },
      }}
    >
      <Grid container spacing={2}>
        <Grid item xs={12} md={6}>
          <Stack
            sx={{ height: { xs: "200px", md: "100%" } }}
            justifyContent={"center"}
            alignItems="center"
          >
            <Box
              component="img"
              src="/favicon/abalone.png"
              sx={{ height: "150px", objectFit: "contain" }}
              id="result"
            />
            <Typography
              variant="h3"
              sx={{
                fontWeight: "bold",
                marginTop: "10px",
                textAlign: "center",
                color: loading ? "gray" : "primary.main",
              }}
            >
              {result || "- - -"}
            </Typography>
          </Stack>
        </Grid>
        <Grid item xs={12} md={6}>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <Typography align="center" variant="h4">
                Age prediction of Abalone
              </Typography>
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Sex"}
                value={data["Sex"]}
                onChange={(e) => onChangeDataHandler("Sex", e.target.value)}
                select
              >
                <MenuItem value={2}>Male</MenuItem>
                <MenuItem value={0}>Female</MenuItem>
                <MenuItem value={1}>Infant</MenuItem>
              </TextField>
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Length"}
                value={data["Length"]}
                onChange={(e) => onChangeDataHandler("Length", e.target.value)}
                type="number"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Diameter"}
                value={data["Diameter"]}
                onChange={(e) =>
                  onChangeDataHandler("Diameter", e.target.value)
                }
                type="number"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Height"}
                value={data["Height"]}
                onChange={(e) => onChangeDataHandler("Height", e.target.value)}
                type="number"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Whole weight"}
                value={data["Whole weight"]}
                onChange={(e) =>
                  onChangeDataHandler("Whole weight", e.target.value)
                }
                type="number"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Shucked weight"}
                value={data["Shucked weight"]}
                onChange={(e) =>
                  onChangeDataHandler("Shucked weight", e.target.value)
                }
                type="number"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Viscera weight"}
                value={data["Viscera weight"]}
                onChange={(e) =>
                  onChangeDataHandler("Viscera weight", e.target.value)
                }
                type="number"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label={"Shell weight"}
                value={data["Shell weight"]}
                onChange={(e) =>
                  onChangeDataHandler("Shell weight", e.target.value)
                }
                type="number"
              />
            </Grid>
            <Grid item xs={12}>
              <Stack
                direction="row"
                alignItems={"center"}
                justifyContent="flex-end"
                spacing={2}
              >
                <a id={"slide-to-result"} href="#result" hidden></a>
                <Button
                  variant="outlined"
                  startIcon={<ClearAllRounded />}
                  onClick={clearHandler}
                  color="inherit"
                >
                  Clear
                </Button>
                <LoadingButton
                  loading={loading}
                  onClick={predictHandler}
                  startIcon={<Settings />}
                  variant="contained"
                >
                  Predict
                </LoadingButton>
              </Stack>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Paper>
  );
};

export default Home;
