class HarmonicOscillator {
    public:
        HarmonicOscillator(float x0, float v0, float m, float k, float vrijeme);
        ~HarmonicOscillator();

        void export_data();
        void restart();

    private:
        void move();
        float _dt;
        float _vrijeme;
        float _m;
        float _k;
        float _t;
        float _x0;
        float _v0;
        float _x;
        float _v;
        float _a;
};